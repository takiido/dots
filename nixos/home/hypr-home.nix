{ pkgs, lib, ... }:

{
  imports = [
    ./common-home.nix
  ];

  home.username = "takiido";
  home.homeDirectory = "/home/takiido";
  home.stateVersion = "25.05";

  programs.home-manager.enable = true;

  programs.foot = {
    enable = true;
  };

  wayland.windowManager.hyprland = {
    enable = true;
    package = pkgs.unstable.hyprland;

    settings = {
      bind = [
        "$mod, Q, exec, foot"
      ];
    };
  };

  programs.nushell.configFile.text = lib.mkAfter ''
    alias rebuild = sudo nixos-rebuild switch --flake /etc/nixos#hypr
  '';

  home.packages = with pkgs; [
    foot
  ] ++ (with pkgs.unstable; [
    hyprpaper
    hyprcursor
  ]);
}
