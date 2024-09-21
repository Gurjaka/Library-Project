{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
    py = pkgs.python3.pkgs;
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [
        fish
        python3
        py.pip
        py.pandas
        py.flask
      ];
      shellHook = ''
        exec fish
        echo "Welcome to ByteMasters project, collaborator!"
      '';
    };
  };
}
