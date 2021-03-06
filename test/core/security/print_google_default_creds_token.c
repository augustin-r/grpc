/*
 *
 * Copyright 2015, Google Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met:
 *
 *     * Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above
 * copyright notice, this list of conditions and the following disclaimer
 * in the documentation and/or other materials provided with the
 * distribution.
 *     * Neither the name of Google Inc. nor the names of its
 * contributors may be used to endorse or promote products derived from
 * this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 */

#include <stdio.h>
#include <string.h>

#include "src/core/security/credentials.h"
#include "src/core/support/string.h"
#include <grpc/grpc.h>
#include <grpc/grpc_security.h>
#include <grpc/support/alloc.h>
#include <grpc/support/cmdline.h>
#include <grpc/support/log.h>
#include <grpc/support/slice.h>
#include <grpc/support/sync.h>

typedef struct {
  grpc_pollset pollset;
  int is_done;
} synchronizer;

static void on_metadata_response(void *user_data,
                                 grpc_credentials_md *md_elems,
                                 size_t num_md,
                                 grpc_credentials_status status) {
  synchronizer *sync = user_data;
  if (status == GRPC_CREDENTIALS_ERROR) {
    fprintf(stderr, "Fetching token failed.\n");
  } else {
    char *token;
    GPR_ASSERT(num_md == 1);
    token = gpr_dump_slice(md_elems[0].value, GPR_DUMP_ASCII);
    printf("\nGot token: %s\n\n", token);
    gpr_free(token);
  }
  gpr_mu_lock(GRPC_POLLSET_MU(&sync->pollset));
  sync->is_done = 1;
  grpc_pollset_kick(&sync->pollset);
  gpr_mu_unlock(GRPC_POLLSET_MU(&sync->pollset));
}

int main(int argc, char **argv) {
  int result = 0;
  synchronizer sync;
  grpc_credentials *creds = NULL;
  char *service_url = "https://test.foo.google.com/Foo";
  gpr_cmdline *cl = gpr_cmdline_create("print_google_default_creds_token");
  gpr_cmdline_add_string(cl, "service_url",
                         "Service URL for the token request.", &service_url);
  gpr_cmdline_parse(cl, argc, argv);

  grpc_init();

  creds = grpc_google_default_credentials_create();
  if (creds == NULL) {
    fprintf(stderr, "\nCould not find default credentials.\n\n");
    result = 1;
    goto end;
  }

  grpc_pollset_init(&sync.pollset);
  sync.is_done = 0;

  grpc_credentials_get_request_metadata(creds, &sync.pollset, service_url,
                                        on_metadata_response, &sync);

  gpr_mu_lock(GRPC_POLLSET_MU(&sync.pollset));
  while (!sync.is_done) grpc_pollset_work(&sync.pollset, gpr_inf_future);
  gpr_mu_unlock(GRPC_POLLSET_MU(&sync.pollset));

  grpc_credentials_release(creds);

end:
  gpr_cmdline_destroy(cl);
  grpc_shutdown();
  return result;
}
