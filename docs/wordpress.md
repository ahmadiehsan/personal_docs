# Wordpress

## Links

- [Curl_Init Error](https://stackoverflow.com/questions/6382539/call-to-undefined-function-curl-init#answer-6382581)
- [Moving A Wordpress Multisite With Duplicator - Snap Creek Software](https://snapcreek.com/duplicator/docs/moving-a-multisite-install-with-duplicator-pro/)
- [What Wordpress Theme Is That?](https://whatwpthemeisthat.com/)
- [Free Divi Layouts - Best Layout Packs For The Divi Wordpress Theme 2019](https://ohklyn.com/free-divi-layouts/)
- [Divi Theme Layouts Directory Lists All The Best Layouts For Divi](https://www.divilayouts.com/)

## Debug

1. Add below lines to `wp-config.php`:

   ```php
   define('WP_DEBUG', false);
   define('WP_DEBUG_DISPLAY', false);
   define('WP_DEBUG_LOG', true);
   ```

2. Logs will store in `project_root/wp-content/debug.log`
