{ config, pkgs, ... }:

{
  imports = [
    ../../modules/stable.nix
    ../../modules/common.nix
    ../../modules/hardware-configuration.nix
  ];

  networking.hostName = "methadone-stable";
  system.nixos.tags = [ "stable" ];
  system.stateVersion = "25.05";
  system.nixos.label = "stable-GNOME";
}
