var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var source = require('vinyl-source-stream');
var buffer = require('vinyl-buffer');
var gutil = require('gulp-util');
var sourcemaps = require('gulp-sourcemaps');
var browserify = require('browserify');
var watchify = require('watchify');
var babelify = require('babelify');
var argv = require('yargs').argv;
var assign = require('lodash.assign');

var package = require('./package.json')
var version = package.version;
const DIST_DIR = 'public/static';
const SASS_DIR = 'sass';

var customOpts = {
    entries: ['./easyphoto/app.js'],
    extensions: ['.jsx'],
    debug: true,
    fullPaths: false,
    noBundleExternal: true,
    transform: [babelify],
    paths: ['./','./easyphoto','./common']
};
argv.production ? customOpts : customOpts.plugin=[watchify];
var opts = assign({}, watchify.args, customOpts);

function doBundle() {
  return b.bundle()
  .on('error', gutil.log.bind(gutil, 'Browserify Error'))
  .pipe(gutil.env.type === 'production' ? source('bundle.js.min') : source('bundle.js'))
  .pipe(buffer())
  .pipe(sourcemaps.init({loadMaps: true}))
  .pipe(gutil.env.type === 'production' ? uglify() : gutil.noop())
  .pipe(sourcemaps.write('./'))
  .pipe(argv.production ? gulp.dest(DIST_DIR + '/prod') : gulp.dest(DIST_DIR + '/dev'))
  .pipe(gutil.noop());
}

var b = browserify(opts);
b.on('update', doBundle);
b.on('log', gutil.log);

gulp.task('js', doBundle);

gulp.task('sass', function() {
  return gulp.src(SASS_DIR + '/easyphoto/easyphoto.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(concat('bundle.css'))
    .pipe(argv.production ? gulp.dest(DIST_DIR + '/prod') : gulp.dest(DIST_DIR + '/dev'))
});

gulp.task('build', ['js', 'sass']);

gulp.task('watch', function() {
  gulp.watch(SASS_DIR + '/easyphoto/*.scss', ['sass']);
});

gulp.task('default', ['build', 'watch']);
