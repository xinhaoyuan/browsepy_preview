import flask
import os
import browsepy
import json

__basedir__ = os.path.dirname(os.path.abspath(__file__))

preview = flask.Blueprint('preview', __name__,
                          url_prefix = '/preview',
                          template_folder = os.path.join(__basedir__,  'templates'),
                          static_folder = os.path.join(__basedir__, 'static'))

extensions = {
    'png': 'image/png'
}

def detect_preview_mimetype(path, sep = os.sep):
    basename = path.rsplit(sep)[-1]
    if '.' in basename:
        ext = basename.rsplit('.')[-1]
        return extensions.get(ext, None)
    return None

@preview.route('/preview_info/<path:path>')
def preview_info(path):
    file = browsepy.file.Node.from_urlpath(path)
    return flask.Response(json.dumps({ "mimetype" : file.type, "url" : "/preview/view/" + path}),
                          mimetype = "text/json")

@preview.route('/view/<path:path>')
def view_file(path):
    # copied from open in browsepy, but explicitly disable cache
    try:
        file = browsepy.file.Node.from_urlpath(path)
        if file.is_file and not file.is_excluded:
            return flask.send_from_directory(file.parent.path, file.name, cache_timeout = 0)
    except OutsideDirectoryBase:
        pass
    flask.abort(404)

# This will be redirected from main.js

@preview.route("/parent-window/", defaults={"path": ""})
@preview.route('/parent-window/<path:path>')
def preview_parent_window(path):
    return flask.render_template("preview_parent_window.html", path = path)

def preview_filter(node, sep = os.sep):
    return isinstance(node, browsepy.file.File)

def register_plugin(manager):

    manager.register_blueprint(preview)
    # Not used
    # manager.register_mimetype_function(detect_preview_mimetype)

    manager.register_widget(
        place = 'styles',
        type = 'stylesheet',
        endpoint = 'preview.static',
        filename = 'css/styles.css')

    manager.register_widget(
        place = 'head',
        type = 'script',
        endpoint = 'preview.static',
        filename = 'javascript/main.js')

    manager.register_widget(
        place = 'entry-actions',
        css = 'preview',
        type = 'button',
        endpoint = 'preview.preview_info',
        text = "Preview",
        filter = preview_filter)
