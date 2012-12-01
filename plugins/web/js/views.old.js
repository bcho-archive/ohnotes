var app = app || {};

$(function($) {
    'use strict';

    /* files list view */
    var FileListView = Backbone.View.extend({
        tagName: 'li',

        template: _.template(app.tmpl.list),

        events: {},

        initialize: function() {
            this.model.on('change', this.render, this);
            this.model.on('visiable', this.toggle, this);
        },

        render: function() {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        },

        toggle: function() {
            this.$el.toggleClass('hidden', this.is_hidden());
        },

        is_hidden: function() {
            return false;
        }
    });

    /* files list info view */
    var FilesListInfoView = Backbone.View.extend({
        el: $('#files-info'),

        template: _.template(app.tmpl.info),

        render: function(info) {
            this.$el.html(this.template(info));
            return this;
        }
    });

    /* file content view */
    app.FileContentView = Backbone.View.extend({
        el: $('#notes-content'),

        template: _.template(app.tmpl.note_buf),

        initialize: function() {
            this.model.on('all', this.render, this);
        },

        render: function() {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        }
    });

    /* app's main view */
    app.AppView = Backbone.View.extend({
        el: '#main',

        events: {
            'keypress #filter input#keywords': 'query_keywords'
        },

        initialize: function() {
            this.files_list = this.$('#notes-list ul.files-list');
            this.filter = this.$('#filter input#keywords');
            this.info = new FilesListInfoView();

            app.notes.on('add', this.list_append, this);
            app.notes.on('reset', this.list_appends, this);
            app.notes.on('all', this.render, this);
            
            app.notes.update_lists();
        },

        render: function() {
            this.info.render({count: app.notes.length});
            return this;
        },

        list_append: function(note) {
            var view = new FileListView({model: note});
            this.files_list.append(view.render().el);
        },

        list_appends: function(notes) {
            _.each(notes.models, this.list_append, this);
        },

        query_keywords: function(e) {
            console.log(this.filter.val());
        }
    });
});
