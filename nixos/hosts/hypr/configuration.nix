{ config, pkgs, ... }:

{
  imports = [
    ../../modules/hypr.nix
    ../../modules/common.nix
    ../../modules/hardware-configuration.nix
  ];

  networking.hostName = "methadone-hypr";
  system.nixos.tags = [ "hypr" ];
  system.stateVersion = "25.05";
  system.nixos.label = "necrodots";
}
