# WordPress

## debug mode

1. add below lines to wp-config.php

   ```php
   define('WP_DEBUG', false);
   define('WP_DEBUG_DISPLAY', false);
   define('WP_DEBUG_LOG', true);
   ```

2. logs will store in `project_root/wp-content/debug.log`
