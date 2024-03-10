'use strict';

const settings = require('../settings');
const { task, src, dest } = require('gulp');
const rename = require('gulp-rename');
const changed = require('gulp-changed');
const imagemin = require('gulp-imagemin');
const imageminWebp = require('imagemin-webp');

// Конвертация контентных изображений в формат WebP
task('webp', function() {
  return src(`${settings.paths.src.images.content}**/*.jpg`)
    .pipe(changed(settings.paths.dest.images.content))
    .pipe(imagemin([imageminWebp({ quality: 80 })]))
    .pipe(rename({ extname: '.webp' }))
    .pipe(dest(settings.paths.dest.images.content));
});
