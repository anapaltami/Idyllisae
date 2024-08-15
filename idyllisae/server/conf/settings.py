r"""
Evennia settings file.

The available options are found in the default settings file found
here:

https://www.evennia.com/docs/latest/Setup/Settings-Default.html

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "Idyllisae"

# Short one-sentence blurb describing your game. Shown under the title
# on the website and could be used in online listings of your game etc.
GAME_SLOGAN = "Temporary game slogan placeholder."

# The url address to your server, like mymudgame.com. This should be the publicly
# visible location. This is used e.g. on the web site to show how you connect to the
# game over telnet. Default is localhost (only on your machine).
SERVER_HOSTNAME = "localhost"

# Lockdown mode will cut off the game from any external connections
# and only allow connections from localhost. Requires a cold reboot.
LOCKDOWN_MODE = True

# Controls whether new account registration is available.
# Set to False to lock down the registration page and the create account command.
NEW_ACCOUNT_REGISTRATION_ENABLED = False

# This is a security setting protecting against host poisoning
# attacks.  It defaults to allowing all. In production, make
# sure to change this to your actual host addresses/IPs.
ALLOWED_HOSTS = ["*"]

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/8.0/interactive/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = "HST"

# How long time (in seconds) a user may idle before being logged
# out. This can be set as big as desired. A user may avoid being
# thrown off by sending the empty system command 'idle' to the server
# at regular intervals. Set <=0 to deactivate idle timeout completely.
IDLE_TIMEOUT = -1

# The idle command can be sent to keep your session active without actually
# having to spam normal commands regularly. It gives no feedback, only updates
# the idle timer. Note that "idle" will *always* work, even if a different
# command-name is given here; this is because the webclient needs a default
# to send to avoid proxy timeouts.
IDLE_COMMAND = "afk"

# If this is true, errors and tracebacks from the engine will be
# echoed as text in-game as well as to the log. This can speed up
# debugging. OBS: Showing full tracebacks to regular users could be a
# security problem -turn this off in a production game!
IN_GAME_ERRORS = True

######################################################################
# Evennia webclient options
######################################################################

# default webclient options (without user changing it)
WEBCLIENT_OPTIONS = {
    # Gags prompts in output window and puts them on the input bar
    "gagprompt": False,
    # Shows help files in a new popup window instead of in-pane
    "helppopup": True,
    # Shows notifications of new messages as popup windows
    "notification_popup": False,
    # Plays a sound for notifications of new messages
    "notification_sound": True,
}

######################################################################
# Game Time setup
######################################################################

# You don't actually have to use this, but it affects the routines in
# evennia.utils.gametime.py and allows for a convenient measure to
# determine the current in-game time. You can of course interpret
# "week", "month" etc as your own in-game time units as desired.

# The time factor dictates if the game world runs faster (timefactor>1)
# or slower (timefactor<1) than the real world.
TIME_FACTOR = 2.0

######################################################################
# Default Account setup and access
######################################################################

# Whether we should create a character with the same name as the account when
# a new account is created. Together with AUTO_PUPPET_ON_LOGIN, this mimics
# a legacy MUD, where there is no difference between account and character.
AUTO_CREATE_CHARACTER_WITH_ACCOUNT = False

# Whether an account should auto-puppet the last puppeted puppet when logging in. This
# will only work if the session/puppet combination can be determined (usually
# MULTISESSION_MODE 0 or 1), otherwise, the player will end up OOC. Use
# MULTISESSION_MODE=0, AUTO_CREATE_CHARACTER_WITH_ACCOUNT=True and this value to
# mimic a legacy mud with minimal difference between Account and Character. Disable
# this and AUTO_PUPPET to get a chargen/character select screen on login.
AUTO_PUPPET_ON_LOGIN = False

# The maximum number of characters allowed by be created by the default ooc
# char-creation command. This can be seen as how big of a 'stable' of characters
# an account can have (not how many you can puppet at the same time). Set to
# None for no limit.
MAX_NR_CHARACTERS = 3


######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")
