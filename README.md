# python-yubikey

Description:
* Python library and tool for acting as a Yubico YubiKey in software (support
  for Yubico OTP only at the moment).
* Why? I became sad I could no longer make lists easily at MIT.

Warning:
* Use this tool at your own risk. I use it in a production environment, but I've
  evaluated my use case. You better evaluate your own.

TODO:
* Write Modhex shim.
* Write Modhex tests.
* Determine Yubico OTP generation algorithm prototype.
* Write OTP generation algorithm.
* Research how Yubico encrypts the generation with the key and how the final
  token is produced.
* As a design consideration, provide a user with a CLI tool that they can invoke
  with counters and configurations stored in ~/.config or the like, with support
  for multiple software "yubikeys" ideally.
* We assume we do not have to keep track of counters. It is trivial however to
  build/write a shim that will store these counters to a file and increment
  them, but some consideration must be taken for the limitations of the two
  relevant counters: `useCtr` is limited to 65536 (and is incremented when a
  real physical YubiKey is plugged in or if `sessionCtr` wraps from `0xff`/255
  to 0), and `sessionCtr` is a 1 byte field that increments by 1 for every
  button press and wraps.
* Research and write other Yubico YubiKey methods, and consider refactoring
  to make this more modular with that in mind.
* REMINDER TO CONTINUOUSLY FIND AND REVIEW TODOs in FILES

Thanks:
* [Yubico YubiKey Manual
  ](https://www.yubico.com/wp-content/uploads/2015/03/YubiKeyManual_v3.4.pdf)
