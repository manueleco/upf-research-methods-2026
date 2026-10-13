#!/usr/bin/env python3
"""Serve the RM panel from its own directory on an available local port."""

import argparse
import errno
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

DOCS = Path(__file__).resolve().parent / "docs"
DEFAULT_PORT = 8321


def create_server(port=DEFAULT_PORT):
    handler = partial(SimpleHTTPRequestHandler, directory=str(DOCS))
    candidates = list(range(port, min(port + 32, 65536))) + [0]
    for candidate in candidates:
        try:
            return ThreadingHTTPServer(("127.0.0.1", candidate), handler)
        except OSError as error:
            if error.errno != errno.EADDRINUSE:
                raise
    raise RuntimeError("No se pudo abrir un puerto local.")


def main():
    parser = argparse.ArgumentParser(description="Abrir el servidor local de Research Methods")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Puerto preferido (por defecto: 8321)")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("El puerto debe estar entre 1 y 65535.")
    if not (DOCS / "index.html").is_file():
        parser.error("No se encuentra el panel en docs/.")
    with create_server(args.port) as server:
        port = server.server_address[1]
        print("Research Methods · servidor local", flush=True)
        if port != args.port:
            print(f"El puerto {args.port} estaba ocupado; se utiliza {port}.", flush=True)
        print(f"Abre http://127.0.0.1:{port}", flush=True)
        print("Para detener este servidor: Ctrl+C.", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor RM detenido.", flush=True)


if __name__ == "__main__":
    main()
