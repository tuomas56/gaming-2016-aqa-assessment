@gulp.task('htmlpdf', ['images', 'html'])
def task_html():
    from gulp_pdfhtml import pdfhtml

    gulp.src('./build/*.html').pipe(pdfhtml('.'))

@gulp.task('html')
def task_html():
	from gulp_markdown import markdown

	gulp.src('*.md').pipe(markdown).pipe(gulp.dest('./build/'))

@gulp.task('images')
def task_images():
    gulp.src('./images/*', binary=True).pipe(gulp.dest('./build/'))

@gulp.task('pandocpdf', ['pandoc', 'images'])
def task_pandoc_pdf():
	from gulp_pandoc import pandocpdf

	gulp.src('./build/*.tex').pipe(pandocpdf('.'))

@gulp.task('pandoc')
def task_pandoc():
	from gulp_pandoc import pandoc

	gulp.src('*.md').pipe(pandoc('./build/'))