module.exports = function(grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        datetime: Date.now(),
        concat: {
            'avionvilleray-js': {
                src: [
                    'bower_components/jquery/jquery.js',
                    'bower_components/bootstrap/dist/js/bootstrap.js',
                    'bower_components/magnific-popup/dist/jquery.magnific-popup.js'
                ],
                dest: 'avionvilleray/static/js/avionvilleray.js'
            }
        },
        uglify: {
            'options': {
                mangle: {toplevel: true},
                squeeze: {dead_code: false},
                codegen: {quote_keys: true}
            },
            'avionvilleray-js': {
                src: 'avionvilleray/static/js/avionvilleray.js',
                dest: 'avionvilleray/static/js/avionvilleray.min.js'
            }
        }
    });


    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');

     grunt.registerTask('default', [
        'concat:avionvilleray-js',
        'uglify:avionvilleray-js'
    ]);
}
