

# Aid4Kids - a generic django based platform for connecting sponsors with sponsored children 

. It is built with [Python][3.7] using the [Django Web Framework][1], can be used by any NGO for helping the children find sponsors. 

This project has the following features:

* Sponsors can register themselves and search for students they want to sponsor
* Manage their profile and unsponsor a sponsored child.
* Admins can see the sponsorships through django admin interface
* Reports for admins are in progress

TODOS
* Automated Payment integration

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv myhealth`
    2. `$ . myhealth/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
