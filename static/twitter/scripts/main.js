import '../styles/main.scss';

(($) => {
  $(document).ready(() => {
   $('myTab a').click(function (e){
    e.preventDeafult();
    $(this).tab('show');
   })
  });
})(jQuery);

/* istanbul ignore if */
if (module.hot) {
  module.hot.accept();
}
