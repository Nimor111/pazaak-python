from django.views.generic import TemplateView


class BoardView(TemplateView):
    template_name = 'board.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['player_board'] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        context['opponent_board'] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        return context
