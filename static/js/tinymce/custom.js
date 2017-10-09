/**
 * Created by Tobin Frost on 13/03/2017.
 */
tinymce.init({
  selector: 'div.rende',
  height: 500,
  menubar: false,
  inline:true,
  language: "fr_FR",
  plugins: [
    'advlist autolink lists link image charmap print preview anchor',
    'searchreplace visualblocks code fullscreen',
    'insertdatetime media table contextmenu paste code textpattern'
  ],
  // toolbar: 'undo redo | insert | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
  content_css: '//www.tinymce.com/css/codepen.min.css'
});