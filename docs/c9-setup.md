# Cloud9 Setup

Instructions to set up scrapy on a new AWS Cloud9 instance.

## Get a new Cloud9 instance.

Seven steps to get a new Cloud9 IDE. It's way easier than it sounds.

1. Log into the AWS Management Console.
2. Search for *Cloud9*. Go forth to Cloud9.
3. On the Cloud9 page, click `Create Environment`.
4. Give it a name and description, then continue.
5. On this next page (Environment Settings), keep all the defaults with one exception: change the Platform from Amazon Linux to Ubuntu Server 18.04 LTS. Then click `Next Step`.
6. Keep defaults on this next page, and just click `Create Environment`.
7. You're in beer time while the thing sets itself up for a few minutes.

## Set up the new Cloud9 instance

1. Update Ubuntu, because why not?

`sudo apt update`

2. Generate an RSA key pair. This is going to help us interact with GitHub. Just hit `Enter` to accept defaults.

`ssh-keygen -t rsa`

3. Enter the following command and copy the output in full.

`cat /home/ubuntu/.ssh/id_rsa.pub`

4. Go to GitHub and [enter a new SSH key](https://github.com/settings/keys). Copy the previous output into the `Key` section. `Title` can be whatever you like.

5. Start up SSH agent.

`eval $(ssh-agent -s)`

6. Add your new identity to the SSH agent.

`ssh-add /home/ubuntu/.ssh/id_rsa`

7. Clone the code repository from GitHub. Use the SSH address.

`git clone git@github.com:chhsinnovation/ca_covid_county_spiders.git`

8. Get into the `ca_covid_county_spiders` folder.

`cd ca_covid_county_spiders/`

9. Install Python dependencies.

`pip3 install -r requirements.txt`

10. Configure `git` with your name and email.

`jon.jensen@chhs.ca.gov:~/environment/ca_covid_county_spiders (master) $ git config --global user.name "Your Name"                                                                      
jon.jensen@chhs.ca.gov:~/environment/ca_covid_county_spiders (master) $ git config --global user.email yourname@whatever.com`

## Run some scrapy

Just check out a crawler to see if it works.

`scrapy crawl sac_county_daily`

Output a JSON file. (Check the output folder to find the file.)

`scrapy crawl sac_county_daily -o output/%(name)s-%(time)s.csv`

Output a JSON file.

`scrapy crawl sac_county_daily -o output/%(name)s-%(time)s.json`

## Still dark magic

Use scrapy's feed export options.

`scrapy crawl sac_county_daily -s FEED_URI='output/%(name)s-%(time)s.json' -s FEED_FORMAT=json`