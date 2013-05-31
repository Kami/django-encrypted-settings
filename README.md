# Django Encrypted Settings

Thin wrapper around Python keyczar bindings which allows you to manage and use
encrypted settings in your Django app.

For more information on how Keyczar works and how to mange keys, visit
the official website at http://www.keyczar.org/.

## Note About Security and Key Storage

This application doesn't do anything with the actual key storage. It's up to
the user to securely store, deploy and manage the access to the secret keys.

For obvious security reasons, secret keys should be stored in a secure place,
separately from the application and its source code.

Good practices for storing keys include:

* Storing keys on a HSM / smart card lLimiting access to the key files if
  storing keys on disk (e.g. using file permissions on Linux)
* Further encrypting the files which store the keys (keyczar supports encrypted
  keysets)

## Installation

```bash
pip install django-encrypted-settings
```

## Usage

TBW

## License

This library is distributed under the [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0.html).
