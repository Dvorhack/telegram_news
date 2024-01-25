let
  pkgs = import <nixpkgs> {};
in
  pkgs.mkShell {
    buildInputs = with pkgs; [
        cargo
        rustc
        openssl
    ];
    nativeBuildInputs = with pkgs; [
        pkg-config
    ];
  }