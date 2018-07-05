var gulp = require('gulp');
var $ = require('gulp-load-plugins')();
var config = require('../config.js').stylesheets;

gulp.task('stylesheets:compile', function(){
    return gulp.src(config.src)
    .pipe($.sass(config.settings))
    .pipe(gulp.dest(config.dest));
});

gulp.task('stylesheets:watch', ['stylesheets:compile'], function() {
  gulp.watch(config.src, ['stylesheets:compile']);
});

gulp.task('stylesheets',['stylesheets:watch']);
