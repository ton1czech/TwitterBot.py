# 🎂 gingy 🎂 [<img alt="License" src="https://img.shields.io/badge/license-MIT-blue.svg">](https://mit-license.org/) [<img alt="Python Version" src="https://img.shields.io/pypi/pyversions/pytube">](https://www.python.org/)

## 💭 **Description**

Python bot to make your Twitter account more active and informative.

---

## ✏ **How To Use**

```
Step 1: Clone the repository
$ git clone https://github.com/ton1czech/gingy

Step 2: Install dependancies
$ pip install -r requirements.txt

Step 3: Setup Twitter developer account
- https://developer.twitter.com/en

Step 4: Setup Heroku account
- https://heroku.com/

Step 5: Setup OpenWeatherMap account
- https://openweathermap.org/

Step 6: Make .env file inside root directory and fill out all credentials (like in .env.example)

Step 7: Change YouTube URL to your's channel URL in 'src/youtube/main.py'

Step 8: Host the application on Heroku

Step 9: In Heroku settings add config variables (exactly same as in .env)
```

---

## 📺 **SHOWCASE**

<div align="center" style="margin: 0 0 50px">
    <h3><strong>Currency prices</strong></h3>
    <img src="https://i.imgur.com/Lj6K5xZ.jpg" height="500">
</div>

<div align="center" style="margin: 0 0 50px">
    <h3><strong>History event</strong></h3>
    <img src="https://i.imgur.com/qLi074P.jpg" height="500">
</div>

<div align="center" style="margin: 0 0 50px">
    <h3><strong>YouTube</strong></h3>
</div>

<div align="center">
    <h3><strong>Weather</strong></h3>
    <img src="https://i.imgur.com/GiHPGIo.jpg" height="500">
</div>

---

## 📜 **LOG**

- **17.04.2021** - _first line_ - Version: 0.1.0
- **18.04.2021** - _format prices[0]_ - Version: 0.2.0
- **18.04.2021** - _scheduling via schedule module_ - Version: 0.2.5
- **18.04.2021** - _added Heroku files_ - Version: 0.3.0
- **18.04.2021** - _moved from schedule to apscheduler_ - Version: 0.3.5
- **18.04.2021** - _added thousand separator for prices[0]_ - Version: 0.3.8
- **18.04.2021** - _removed unnecessary lines_ - Version: 0.4.0
- **21.04.2021** - _making this project multifile_ - Version: 0.5.0
- `21.04.2021 - STABLE RELEASE - Version: 0.5.0`
- **21.04.2021** - _added historical facts[1]_ - Version: 0.5.5
- **22.04.2021** - _historical facts 100% functional[1]_ - Version: 0.5.8
- `22.04.2021 - STABLE RELEASE - Version: 0.6.0`
- **24.04.2021** - _improvements on historical facts[1]_ - Version: 0.6.1
- **25.04.2021** - _preparing to post tweet when I upload video[2]_ - Version: 0.6.2
- **29.04.2021** - _decide to use selenium for videos (requests remake is possible)[2]_ - Version: 0.6.5
- **30.03.2021** - _functionality to check if the video is already tweeted[2]_ - Version: 0.6.8
- **02.05.2021** - _optimizing tweet latest youtube video[2]_ - Version: 0.6.9
- `02.05.2021 - STABLE RELEASE - Version: 0.7.0`
- **17.05.2021** - _using Chromedriver instead of geckodriver[2]_ - Version: 0.7.1
- **04.06.2021** - _deleting Chromedriver and using pytube_[2] - Version: 0.7.4
- **05.06.2021** - _weather forecast(new module)[3]_ - Version: 0.7.5
- **05.06.2021** - _custom emoji for every type of weather[3]_ - Version: 0.7.6
- **05.06.2021** - _simple error handling (if x=None pass)_ - Version: 0.7.8
- `05.06.2021 - STABLE RELEASE - Version: 0.8.0`
- **06.06.2021** - _calling functions directly from main file_ - Version: 0.8.5
- **07.06.2021** - _refactoring code_ - Version: 0.8.9

---

## 📎 **License**

MIT License

Copyright (c) [2021] [Daniel Anthony Baudyš]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## **Author Info**

- Twitter - [@ton1czech](https://twitter.com/ton1czech)
- Instagram - [@ton1czech](https://instagram.com/ton1czech)
