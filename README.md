# Example Bulk Machine Deactivation

This is an example of how to deactivate a license's machines in bulk using
Keygen's API, written in Python. Depending on how many machines you're
deactivating, you may need to implement rate-limiting behavior.

## Running the example

First up, configure a few environment variables:

```bash
# Your Keygen account ID. Find yours at https://app.keygen.sh/settings.
export KEYGEN_ACCOUNT_ID="YOUR_KEYGEN_ACCOUNT_ID"

# A Keygen license ID. Used for deactivating the license's machines.
export KEYGEN_LICENSE_ID="A_KEYGEN_LICENSE_ID"

# A Keygen license ID. Used for API authentication.
export KEYGEN_LICENSE_KEY="A_KEYGEN_LICENSE_KEY"
```

You can either run each line above within your terminal session before
starting the app, or you can add the above contents to your `~/.bashrc`
file and then run `source ~/.bashrc` after saving the file.

Next, install dependencies with [`pip`](https://packaging.python.org/):

```
python3 -m pip install -r requirements.txt
```

To perform a bulk deactivation, run the script:

```
python3 main.py
```

The script will paginate through the license's machines and deactivate each one.

## Questions?

Reach out at [support@keygen.sh](mailto:support@keygen.sh) if you have any
questions or concerns!
