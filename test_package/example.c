#include "libimagequant.h"

static void test_fixed_colors()
{
    liq_attr *attr = liq_attr_create();

    unsigned char dummy[4] = {0};
    liq_image *img = liq_image_create_rgba(attr, dummy, 1, 1, 0);

    liq_image_add_fixed_color(img, (liq_color){0, 0, 0, 0});

    liq_result *res = liq_quantize_image(attr, img);

    const liq_palette *pal = liq_get_palette(res);

    liq_result_destroy(res);
    liq_image_destroy(img);
    liq_attr_destroy(attr);
}

int main(void)
{
    test_fixed_colors();
    return 0;
}