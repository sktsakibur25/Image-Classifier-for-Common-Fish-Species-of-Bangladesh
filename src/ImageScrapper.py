from icrawler.builtin import BingImageCrawler
import os

scientific_names = [
    "Labeo rohita",
    "Catla catla",
    "Cirrhinus cirrhosus",
    "Tenualosa ilisha",
    "Anabas testudineus",
    "Oreochromis niloticus",
    "Ompok pabda",
    "Heteropneustes fossilis",
    "Clarias batrachus",
    "Wallago attu",
    "Pangasius pangasius",
    "Chitala chitala",
    "Labeo bata",
    "Amblypharyngodon mola",
    "Channa punctata",
    "Channa striata",
    "Channa marulius",
    "Harpadon nehereus",
    "Corica soborna",
    "Mastacembelus armatus"
]

local_names = [
    "Rui",
    "Katla",
    "Mrigal",
    "Hilsa",
    "Koi",
    "Tilapia",
    "Pabda",
    "Shing",
    "Magur",
    "Boal",
    "Pangas",
    "Chitol",
    "Bata",
    "Mola",
    "Taki",
    "Shoal",
    "Gajar",
    "Loitta",
    "Kachki",
    "Baim"
]

os.makedirs('images', exist_ok=True)

for i, (sci_name, local_name) in enumerate(zip(scientific_names, local_names)):
    try:
        crawler = BingImageCrawler(
            feeder_threads=1,
            parser_threads=1,
            downloader_threads=4,
            storage={'root_dir': f'images/{local_name.replace(" ", "_")}'}
        )
        crawler.crawl(keyword=f'{sci_name} fish', max_num=100)
        print(f"Downloaded images for {local_name}")
    except Exception as e:
        print(f"Error downloading {local_name}: {str(e)}")
        continue