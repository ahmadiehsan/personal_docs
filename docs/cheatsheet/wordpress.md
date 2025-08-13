# Wordpress

## Debug

1. Add below lines to `wp-config.php`:

  ```php
  define('WP_DEBUG', false);
  define('WP_DEBUG_DISPLAY', false);
  define('WP_DEBUG_LOG', true);
  ```

2. Logs will store in `project_root/wp-content/debug.log`
