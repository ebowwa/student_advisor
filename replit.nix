{pkgs}: {
  deps = [
    pkgs.from api._assist.async_scraper import AsyncScraper
    pkgs.libxcrypt
  ];
}
