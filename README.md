## Live App Demo: [RP2 Single-Core Processor Server](http://216.250.8.62:2024/diaries/newsfeed-view/)

```
🚀 Give a Star ⭐️ & Fork to this project ... Happy coding! 🤩`
```

## Table of Contents

- [What makes RP2 special?](#what-makes-rp2-special)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## What makes RP2 special?

RP2 is a rapidly-growing open-source next generation project and task management system! Work with your team members and interact with the gamification system!

Template from [Vikinger](https://themeforest.net/item/vikinger-social-community-and-marketplace-html-template/25715500) used.

![RP2 Dashboard - Modern Vikinger UI for managing your project](https://img.themesinfo.com/i/2/1645/template-wordpress-vikinger-buddypress-social-community-pqqwe-o.jpg)

## Installation [examples on Linux@Ubuntu]

Note:
The `dev` branch is the development version of RP2 and it may be unstable. To use the latest stable version, download it from the [Releases](https://github.com/Hojagulyyev/rp2/releases/) page or switch to a release tag.

### Terminal 1
The fastest way to develop with RP2 is by using python [virtualenv](https://pypi.org/project/virtualenv/) library

install virtualenv if it's not installed

`pip install virtualenv`

and run the following commands:

`git clone -b main https://github.com/Hojagulyyev/rp2.git`

`cd rp2`

`virtualenv venv`

`. source/bin/activate`

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

### Terminal 2

Just installing Celery, however, isn’t enough. 
If you attempt to run the task queue, you’ll notice that Celery first 
seems to start up fine but then displays an error message that 
indicates that Celery can’t find a message broker.

`sudo apt install redis`

Open another terminal or linux service in server
and run celery workers

`celery -A rp2 worker --loglevel=info`

### Terminal 3

Open another terminal or linux service. 
You should change permission access mode (chmod) of these files

`chmod -R 777 celerybeat-schedule venv`

and run celery beat

`celery -A rp2 beat`

You’ve successfully arranged the puzzle pieces necessary to run the project.

## Contributing

Use the `dev` branch to contributing.
We love your contributions and do our best to provide you with mentorship and support.

## License

Disclaimer: Everything you see here is open and free to use as long as you comply with the [license](https://github.com/Hojagulyyev/rp2/blob/main/LICENSE). There are no hidden charges. We promise to do our best to fix bugs and improve the code.

#### Crafted with ❤️ by [Contributors](https://github.com/Hojagulyyev/rp2/graphs/contributors)
