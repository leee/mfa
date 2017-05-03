# python-yubikey

Description:
* Python library and tool for acting as a Yubico YubiKey in software (support
  for Yubico OTP only at the moment).
* Why? I became sad I could no longer make lists easily at MIT.

Warning:
* Use this tool at your own risk. I use it in a production environment, but I've
  evaluated my use case. You better evaluate your own.

TODO:
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
* serial numbers?
  (which come in dec, hex, and mod form: 3262790, 31c946, ebrkfh) figure out
  what these are for, apart from unique ids for physical yubikey tokens.
* rebrand away from `python-yubikey` when we turn into a tool.
* REMINDER TO CONTINUOUSLY FIND AND REVIEW TODOs in FILES

CLI tool wish list:
* available via package managers for major distributions (apt, brew, yum, ...
  windows? chocolatey?)

```
$ # comes with tab completion for commands and configuration-slots
$ yubikey help
    new: create a new configuration slot, either as a one-liner or with prompts
    press: press a configuration slot
    default: set a default configuration slot
    help: this message
$ yubikey press configuration-slot
...
$ # suppose you have a "configuration slot" called "test-otp"
$ yubikey new test-otp "vv uj fr el ne rh" "a2 c3 f9 8d 67 od" "128 bit crap"
$ yubikey new test-otp
    public identity: vv uj fr el ne rh (or random)
    private identity: a2 cf9 8d 67 od
    secret key: insert 16 bytes of secret sauce here
$ yubikey press test-otp
cccjgjgkhcbbirdrfdnlnghhfgrtnnlgedjlftrbdeut
$ yubikey default test-otp
$ yubikey
cccjgjgkhcbbirdrfdnlnghhfgrtnnlgedjlftrbdeut
$ # maybe include shortcut aliases
$ # auto copy to keyboard
```

Thanks:
* [Yubico YubiKey Manual
  ](https://www.yubico.com/wp-content/uploads/2015/03/YubiKeyManual_v3.4.pdf)
