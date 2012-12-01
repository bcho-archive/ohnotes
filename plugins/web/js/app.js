var app = app || {};

$(function() {
    'use strict';

    /* Kick off */
    app.current_id = app.current_id || 0;
    app.shown_notes = new app.Query();

    app.help_msg = new app.Note;
    app.help_msg.set('content', app.tmpl.help_msg);

    new app.AppView();

    /* we fire the first update */
    app.notes.trigger('update');
});
