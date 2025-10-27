{ pkgs, ... }:

{
  programs.nushell = {
    enable = true;

    configFile.text = ''
      $env.config = {
        show_banner: false
      }

      def rebuild-all [] {
        sudo nixos-rebuild boot --flake /etc/nixos#stable
        sudo nixos-rebuild boot --flake /etc/nixos#hypr
      }

      def cleanup [] {
        sudo nix-collect-garbage --delete-old
        sudo nix-store --optimize
      }
    '';

    envFile.text = ''
      # Nushell environment configuration
    '';

    loginFile.text = ''
      fastfetch
    '';
  };

  programs.git = {
    enable = true;
    userName = "takiido";
    userEmail = "takiid0@proton.me";

    extraConfig = {
      init = {
        defaultBranch = "master";
      };
      pull = {
        rebase = false;
      };
    };
  };

  programs.ssh = {
    enable = true;

    matchBlocks = {
      "github.com" = {
        hostname = "github.com";
        user = "git";
        identityFile = "~/.ssh/id_ed25519";
      };
    };
  };

  programs.fastfetch = {
    enable = true;
    settings = {
      logo = {
        source = "nixos";
        padding = {
          right = 1;
        };
      };
      display = {
        separator = " -> ";
      };
      modules = [
        "title"
        "separator"
        "os"
        "kernel"
        "uptime"
        "packages"
        "shell"
        "de"
        "wm"
        "cpu"
        "memory"
        "colors"
      ];
    };
  };
}
