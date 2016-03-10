from sys import exit


class Scene(object):

    def enter(self):
        print 'Unfinished'
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening
        last_scene = self.scene_map.next_scene('ending')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Map(object):

    scenes = {

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        n = Map.scenes.get(scene_name)
        return n

    def opening_scene(self):
        return self.next_scene(self.start_scene)
