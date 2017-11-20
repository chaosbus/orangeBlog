/**
 * Created by Joe on 2017/11/20.
 */
// dropdown
$('.dropdown-toggle').dropdown()

// add active
$('.nav-pills').find('a').each(function () {
    if (this.href == document.location.href || document.location.href.search(this.href) >= 0) {
        $(this).parent().addClass('active'); // this.className = 'active';
    }
});