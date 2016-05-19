import downloader
import ooxx_parser
import img_downloader


download = downloader.download
parse = ooxx_parser.parse
img_download = img_downloader.Download_image()

def main():
    page_url_a = "http://jandan.net/ooxx/page-"
    page_url_num = 1549

    while page_url_num <= 1961:
        page_url = page_url_a + str(page_url_num)

        page_html = download(page_url)
        print(page_url_num)
        image_urls = parse(page_html)

        for image_url in image_urls:
            print(image_url)
            img_download.download(image_url)

        page_url_num += 1

if __name__ == "__main__":
    main()
