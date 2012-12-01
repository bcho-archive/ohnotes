var app = app || {};

(function() {
    'use strict';

    var list = '<li><a href="#note/<%= id %>"><%= name %></a></li>';
    var current = ' / current <span class="current"><%= name %></span>';
    var info = '<p>total: <%= count %><%= current %></p>';
    var note_buf = '<pre class="buf"><%= content %></pre>';
    var error = 'Oops, somethings went wrong...'
    var help_msg = '# Here are your notes';

    app.tmpl = {
        list: list,
        current: current,
        info: info,
        note_buf:  note_buf,
        error: error,
        help_msg: help_msg
    };
} ());
