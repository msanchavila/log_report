# Log Report

The purpose of this project is to create a reactive dash board from static log files. 

## Prompt

There are 2 services that create daily access log files. Your task is to parse out each log and create a daily report which include:
1. Number of visits
2. Number of users
3. URLs/Endpoints visited
4. Number HTTP requests
5. etc

The reports must allow filtering by a user, time, URL or HTTP request.

## Prerequisites

* [Python 3](https://www.python.org/downloads/)
* [Anaconda](https://docs.anaconda.com/anaconda/install/windows/)

## Installation

1. Navigate to project directory
2. Clone project into local environment

    `> git clone https://github.com/msanchavila/log_report.git`

3. Navigate into project directory

    `> cd log_report`

4. Create virtual environment

    `> conda env create -f environment.yml`

5. Activate virtual environment

    `> conda activate log_report`

If all commands are completed successfully, your command line prompt should look similar to this

`(log_report) > `

This means your `log_report` virtual environment is active and ready to use! :)

## Logs

For this project, we'll generate fake log data using [flog](https://github.com/mingrammer/flog). Thanks to [mingrammer](https://github.com/mingrammer) for creating this awesome tool!

### Log Example

Here is an example stream of access logs; we'll be using [apache_common](https://httpd.apache.org/docs/1.3/logs.html) format. 

```
172.194.108.174 - dickens1165 [15/07/2019:21:51:41 -0700] "HEAD /channels" 504 29356
224.174.146.179 - greenholt4303 [15/07/2019:21:51:41 -0700] "PATCH /extensible/one-to-one" 416 19997
95.137.83.102 - - [15/07/2019:21:51:41 -0700] "PUT /cultivate/cultivate/synergies/web-readiness" 500 10109
139.177.23.215 - - [15/07/2019:21:51:41 -0700] "PATCH /benchmark/incubate/bleeding-edge/best-of-breed" 201 27038
111.50.115.103 - - [15/07/2019:21:51:41 -0700] "HEAD /niches/collaborative/value-added" 204 22653
234.74.22.119 - - [15/07/2019:21:51:41 -0700] "PUT /seamless/mesh/web-enabled" 504 10127
154.215.239.201 - - [15/07/2019:21:51:41 -0700] "PUT /roi/technologies/reinvent" 502 23593
242.232.48.137 - gleason4123 [15/07/2019:21:51:41 -0700] "PATCH /extend/synthesize/b2c/interfaces" 304 17504
```

Each service will generate its own rotating log files; as they become too large a new log file will continue the activity stream and will have an increased counter.

```
    20190715_ServiceA.log
    20190715_ServiceA1.log
    20190715_ServiceA2.log
    20190715_ServiceA3.log
        ...
    20190715_ServiceAn.log
```

### Log Generation

In the home directory of the project, use the following command to generate log files in `logs` directory.

`> python generate_logs.py`

You should be able to see a new directory called `logs` filled with 20 log files for `MemLourde` and `AutoMeme`.
