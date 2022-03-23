"""
    This module is just for future reference.
    I worked hard on this one, as it turns out
    to validate js files are way hard and complicated an
    anticipated. Service are few and not reliable,
    especially when the files are minified.

    My code worked very well, and I successfully
    sent multiple files to the service and got
    the results successfully, but with too many js
    errors which would ultimately create distrust
    and hurt webalyzer.
"""

self.request_js_files_falsy = False


def request_js_errors(scripts):
    """ Function to send files to validation service """

    ewd = re.split(WHOLE_DOMAIN, str(self.url))[1]
    processing_count = 0
    for script in scripts:
        processing_count += 1
        print("Processing file: ", processing_count)

        with requests.Session() as re_s:
            re_s = cfscrape.create_scraper()
            re_s.headers = self.headers
            res = re_s.get(self.javascript + ewd + script)

            self.js_data.append(BeautifulSoup(
                res.content, 'html5lib'))
        sleep(6)


def request_js_files():
    """ Function to first scrape js files from website"""

    with requests.Session() as re_s:
        re_s = cfscrape.create_scraper()
        res = re_s.get(self.url)

        data = BeautifulSoup(res.content, 'html5lib')

        scripts = data.find_all('script')

    all_scripts = []
    for script in scripts:
        with_source = script.get_attribute_list('src')

        if with_source[0] is None:
            continue
        all_scripts.append(with_source[0])

        if DOMAIN.match(str(with_source[0])):
            extract_domain = re.split(DOMAIN, with_source[0])

            for line in extract_domain:
                if line is None or line == '':
                    continue

                all_scripts.remove(with_source[0])

    self.request_js_files_falsy = True
    request_js_errors(all_scripts)


if not self.request_js_files_falsy:
    request_js_files()
