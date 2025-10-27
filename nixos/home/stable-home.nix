{ pkgs, lib, ... }:

{
  imports = [
    ./common-home.nix
  ];

  home.username = "takiido";
  home.homeDirectory = "/home/takiido";
  home.stateVersion = "25.05";

  programs.home-manager.enable = true;

  dconf.settings."org/gnome/desktop/interface" = {
    color-scheme = "prefer-dark";
  };

  programs.nushell.configFile.text = lib.mkAfter ''
    alias rebuild = sudo nixos-rebuild switch --flake /etc/nixos#stable
  '';

  home.packages = with pkgs; [
    gnome-tweaks
    gnome-extension-manager
  ];
}
