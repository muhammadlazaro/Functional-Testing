FROM php:8.0-apache

# Copy isi folder aut2026-main langsung ke web root
COPY aut2026/aut2026-main/ /var/www/html/

RUN chown -R www-data:www-data /var/www/html \
    && chmod -R 755 /var/www/html

EXPOSE 80
