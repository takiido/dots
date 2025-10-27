{ config, pkgs, ... }:

{
  time.timeZone = "America/Winnipeg";

  nix.settings.experimental-features = [ "nix-command" "flakes" ];
  nix.gc.automatic = true;
  nix.gc.dates = "weekly";
  nix.gc.options = "--delete-older-than 14d";

  users.users.takiido = {
    isNormalUser = true;
    description = "takiido";
    extraGroups = [ "wheel" "networkmanager" "video" "audio" ];
    shell = pkgs.nushell;
  };

  i18n.defaultLocale = "en_CA.UTF-8";
  nixpkgs.config.allowUnfree = true;

  virtualisation.libvirtd.enable = true;
  virtualisation.spiceUSBRedirection.enable = true;

  environment.systemPackages = with pkgs; [
      code-cursor
      fastfetch
      firefox
      git
      gnome-boxes
      heroic
      neovim
      nushell
      spotify
      starship
      vscode
  ] ++ (with pkgs.unstable; [
      zed-editor
  ]);
}
