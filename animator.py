from maya import cmds
import random

def generate_animation(duration_value, step_value,

    translate_x_max, translate_y_max, translate_z_max,
    translate_x_min, translate_y_min, translate_z_min,

    rotate_x_max, rotate_y_max, rotate_z_max,
    rotate_x_min, rotate_y_min, rotate_z_min,

    scale_x_max, scale_y_max, scale_z_max,
    scale_x_min, scale_y_min, scale_z_min):




    cmds.undoInfo(openChunk=True) #ctrl z

    try:


        random_step = random.randint(1, int(step_value))

        nb_keyframe = ((duration_value - 1) // random_step - 1)

        selection = cmds.ls(selection=True, transforms=True)

        cmds.cutKey(selection, clear=True)

        cmds.playbackOptions(min=1, max=duration_value)


        for obj in selection:


            # Keyframes initiales
            cmds.setKeyframe(obj, attribute=["translateX","translateY","translateZ"], value=0, time=1)
            cmds.setKeyframe(obj, attribute=["rotateX","rotateY","rotateZ"], value=0, time=1)
            cmds.setKeyframe(obj, attribute=["scaleX","scaleY","scaleZ"], value=1, time=1)


            # Translate
            for i in range(nb_keyframe):

                random_translate_x = random.uniform(float(translate_x_min), float(translate_x_max))
                random_translate_y = random.uniform(float(translate_y_min), float(translate_y_max))
                random_translate_z = random.uniform(float(translate_z_min), float(translate_z_max))

                keyframe_time = 1 + ((i + 1) * random_step)

                cmds.setKeyframe(obj, attribute="translateX", value=random_translate_x, time=keyframe_time)
                cmds.setKeyframe(obj, attribute="translateY", value=random_translate_y, time=keyframe_time)
                cmds.setKeyframe(obj, attribute="translateZ", value=random_translate_z, time=keyframe_time)


            # Rotate
            for i in range(nb_keyframe):

                random_rotate_x = random.uniform(float(rotate_x_min), float(rotate_x_max))
                random_rotate_y = random.uniform(float(rotate_y_min), float(rotate_y_max))
                random_rotate_z = random.uniform(float(rotate_z_min), float(rotate_z_max))

                keyframe_time = 1 + ((i + 1) * random_step)

                cmds.setKeyframe(selection, attribute="rotateX", value=random_rotate_x, time=keyframe_time)
                cmds.setKeyframe(selection, attribute="rotateY", value=random_rotate_y, time=keyframe_time)
                cmds.setKeyframe(selection, attribute="rotateZ", value=random_rotate_z, time=keyframe_time)


            # Scale
            for i in range(nb_keyframe):

                random_scale_x = random.uniform(float(scale_x_min), float(scale_x_max))
                random_scale_y = random.uniform(float(scale_y_min), float(scale_y_max))
                random_scale_z = random.uniform(float(scale_z_min), float(scale_z_max))

                keyframe_time = 1 + ((i + 1) * random_step)

                cmds.setKeyframe(obj, attribute="scaleX", value=random_scale_x, time=keyframe_time)
                cmds.setKeyframe(obj, attribute="scaleY", value=random_scale_y, time=keyframe_time)
                cmds.setKeyframe(obj, attribute="scaleZ", value=random_scale_z, time=keyframe_time)


            # Keyframes finales
            cmds.setKeyframe(obj, attribute=["translateX","translateY","translateZ"], value=0, time=duration_value) 
            cmds.setKeyframe(obj, attribute=["rotateX","rotateY","rotateZ"], value=0, time=duration_value)
            cmds.setKeyframe(obj, attribute=["scaleX","scaleY","scaleZ"], value=1, time=duration_value)

    finally:
        cmds.undoInfo(closeChunk=True) #ctrl z

   