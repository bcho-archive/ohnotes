var app = app || {};

$(function($) {
    'use strict';

    /* files item view */
    var FileItem = Backbone.View.extend({
        tagName: 'li',
        template: _.template(app.tmpl.list),
       
        initialize: function() {
            this.model.on('change', this.render, this);
            this.model.on('toggle', this.toggle, this);
        },

        render: function() {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        },

        toggle: function() {
            if (_.indexOf(app.shown_notes.get('ids'), this.model.get('id')) === -1)
                this.$el.hide();
            else
                this.$el.show();
        }
    });

    /* files list info view */
    var FilesInfo = Backbone.View.extend({
        el: $('#files-info'),
        template: _.template(app.tmpl.info),
        current_template: _.template(app.tmpl.current),

        info: function() {
            var current = app.notes.get(app.current_id);
            if (current !== undefined)
                var current_info = this.current_template(current.toJSON());

            if (app.shown_notes.get('word') !== null)
                var count = app.shown_notes.get('ids').length;
            else
                var count = app.notes.length;

            return {
                count: count,
                current: current_info
            };
        },

        initialize: function() {
            app.notes.on('update', this.render, this);
        },

        render: function() {
            this.$el.html(this.template(this.info()));
            return this;
        }
    });

    /* note buffer view */
    var NoteContent = Backbone.View.extend({
        el: $('#notes-content'),
        template: _.template(app.tmpl.note_buf),
        
        render: function() {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        },

        show_error: function(msg) {
            msg = msg || app.tmpl.error;
            this.$el.html(this.template({content: msg}));
            return this;
        }
    });

    /* filter view */
    var Filter = Backbone.View.extend({
        el: $('#filter input#keywords'),

        value: function() {
            return this.$el.val();
        }
    });

    /* main app view */
    app.AppView = Backbone.View.extend({
        el: '#main',

        events: {
            'change #filter input#keywords': 'find'
        },

        initialize: function() {
            this.files_list = this.$('#notes-list ul.files-list');
            this.info = new FilesInfo();
            this.buffer = new NoteContent();
            this.filter = new Filter();

            app.notes.on('add', this.append_note, this);
            app.notes.on('reset', this.append_notes, this);
            app.notes.on('update', this.update_buffer, this);
            app.notes.on('all', this.render, this);
            
            app.shown_notes.on('change:word', this.query_word, this);
            app.shown_notes.on('change:ids', this.toggle_all, this);

            app.notes.update_lists();
        },

        append_note: function(note) {
            var view = new FileItem({model: note});
            this.files_list.append(view.render().el);
        },

        append_notes: function(notes) {
            notes.each(this.append_note, this);
        },

        update_buffer: function() {
            var note = app.notes.get(app.current_id) || app.help_msg;
            this.buffer.model = note;
            note.on('all', this.buffer.render, this.buffer);
            /* show instruction */
            if (note.get('id') === 0)
                note.trigger('show');
            /* check out for the content */
            else
                note.fetch();
        },

        find: function() {
            var w = this.filter.value();
            if (w !== '')
                app.shown_notes.set('word', w);
            else
                app.shown_notes.reset();
        },

        query_word: function() {
            /* we are not going to query word in init state */
            if (app.shown_notes.get('word') === null)
                return;
            app.shown_notes.fetch({
                'error': function(c, resp, o) {
                    o.context.buffer.show_error('Not found.');
                },
                /* FIXME trigger 404 error msg */
                'context': this
            });
        },

        toggle_all: function() {
            _.each(app.notes.models, function(note) {
                note.trigger('toggle')
            });
        },

        render: function() {
            this.info.render();
            return this;
        }
    });
});
