import os
class AutoCrawler:
    def __init__(self, skip_already_exist=True,
                 n_threads=4, do_google=True,
                 do_naver=True,
                 download_path='download',
                 full_resolution=False,
                 face=False):

        self.skip = skip_already_exist
        self.n_threads = n_threads
        self.do_google= do_google
        self.do_naver = do_naver
        self.download_path = download_path
        self.full_resovation = full_resolution
        self.face = face

        os.makedirs('./{}'
                    .format(self.download_path),
                    exist_ok=True)
    def do_crawling(self):
        keyswords = self.get_keywords()
        tesks = []
        for keyword in keywords:
            dir_name = '{}/{}'.format(self.download_path, keyword)
            if os.path.exists(os.path.join(os.getcwd(), dir_name)) and self.skip:
                continue

        if self.do google:
            if self.full_resovation:
                tasks.append([keyword, Sites.GOOGLE_FULL])
            else:
                tasks.append([keyword, Sites.GOOGLE])

        if self.do.naver:
            if self.full_resovation:
                tasks.append([keyword, Sites.NAVER_FULL])
            else:
                tasks.append([keyword, Sites.NAVER])

    pool = Pool(self.n_threads)
    pool.map_async(self.download, tasks)
    pool.close()
    pool.join()
    def download_from_site(self, keyword, site_code):
        site_name = Sites.get_text(site_code)
        add -url = Sites.get_text(site_code) if slf.face else ""

        try:
            collect = CollectLinks()
        except Exception as e:
            print('Error occured while initializing chromedriver - {}'.format(e))
            return

        try:
            print('Collecting links...{} from {}' .format(keyword, site name))

            if site_code == Sites.GOOGLE:
                links = collect.naver(keyword, add_url)

            elif site_code == Sites.NAVER:
                links = collect.naver(keyword, add_url)

            elif site_code == Sites.GOOGLE_FULL:
                Links = collect.google_full(keyword, add_url)

            else:
                print('Invalid Site Code')
                link = []

            print('Downloading images from collected links... {} from {}'.format(keyword,site_name))
            self.download_images(keyword, links, site_name)

if '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--skip', tpye=str, default='true')
    parser.add_argument('--threads', tpye=int, default=4)
    parser.add_argument('--google', type=str, default= 'true')
    parser.add_argument('--naver', type=str, default='true')
    parser.add_argument('--full', type=str, default='false')
    parser.add_argument('--face', tpye=str, default='false')
    args = parser.parse_args()

    _skip = False if str(args.skip).lower() == 'false' else True
    _threads = args.threads
    _google = False if str(args.google).lower() == 'false' else True
    _naver = False if str(args.naver).lower() == 'false' else True
    _full = False if str(args.full).lower() == 'false' else True
    _face = False if str(args.face).lower() == 'false' else True

    print('Option - skip :{}, threads :{}, google: {}, naver:{},'
          'full_resovation:{}, face:{}'.format(_skip, _threads,
                                               _google, _naver, _full, _face))

    crawler = AutoCrawler(skip_already_exist=_skip, n_threads=_threads, do_google=_google,
                          do_naver= _naver, full_resolution= _full, face=_face)
    crawler.do_crawling()

