OnkyoISCP Plugin
------------------------------------------------------------------------------

This plugin allows you to send commands to your Onkyo and to receive events.

The list of supported commands per device can be found in the ISCP protocol
file. This file is officially under NDA so I am not allowed to host it here,
but Michael Elsdorfer has the file available on his site:
http://michael.elsdoerfer.name/onkyo/ISCP-V1.21_2011.xls

Example commands:

 - Set the volume to `45`: `MVL2D` (Master Volume in hex, `0x2D = 45`)
 - Increase the volume: `MVLUP`
 - Decrease the volume: `MVLDOWN`

Install
==============================================================================

 - Download: https://github.com/WoLpH/EventGhost-Onkyo-ISCP-plugin/archive/master.zip
 - Unzip the `master.zip` file to `C:\Program Files (x86)\EventGhost\plugins`
 - Restart EventGhost
 - Add the plugin to autostart
 - Configure the plugin so the IP and ports are correct. The default port is `60128`

