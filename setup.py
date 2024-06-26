from setuptools import find_packages, setup

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name="jupyterhub-nativeauthenticator",
    version="1.2.0",
    description="JupyterHub Native Authenticator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jupyterhub/nativeauthenticator",
    author="Leticia Portella",
    author_email="leportella@protonmail.com",
    license="3 Clause BSD",
    packages=find_packages(),
    entry_points={
        # Thanks to this, user are able to do:
        #
        #     c.JupyterHub.authenticator_class = "native"
        #
        # ref: https://jupyterhub.readthedocs.io/en/4.0.0/reference/authenticators.html#registering-custom-authenticators-via-entry-points
        #
        "jupyterhub.authenticators": [
            "native = nativeauthenticator:NativeAuthenticator",
        ],
    },
    install_requires=["jupyterhub>=1.3", "bcrypt", "pyotp", "qrcode"],
    extras_require={
        "test": [
            "notebook>=6.4.1",
            "pytest",
            "pytest-asyncio",
            "pytest-cov",
        ],
    },
    include_package_data=True,
)
