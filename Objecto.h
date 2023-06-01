#ifndef LEARNOPENGL_OBJETO_H
#define LEARNOPENGL_OBJETO_H
#include <glad/glad.h>
#include "include/glm/glm.hpp"
#include "include/glm/gtx/string_cast.hpp"
#include "include/glm/gtc/matrix_transform.hpp"
#include "include/glm/gtc/type_ptr.hpp"
#include <vector>
#include "include/shader_s.h"
using namespace std;
using namespace glm;

class Objeto {
public:
    vector<vec3> positions;
    vector<vec3> normals;
    vector<vec2> textureCoords;
    vector<GLuint> indices;
    GLuint indices_size;
    GLuint vao;
    mat4 model;
    bool visible=true;
    GLint POSITION_ATTRIBUTE=0, NORMAL_ATTRIBUTE=1, TEXCOORD0_ATTRIBUTE=8;
    virtual GLuint setup()=0;
    virtual void display(Shader &sh)=0;
};

class Esfera:public Objeto{
public:
    vec3 centro;
    float radius;
    int slices, stacks;
    Esfera() {
        centro = vec3(0.0);
    }
    Esfera(vec3 _centro) {
        centro = _centro;
    }
    Esfera(vec3 _centro, float _radius, int _slices, int _stacks) {
        centro = _centro;
        radius = _radius;
        slices = _slices;
        stacks = _stacks;
    }
    GLuint setup();

    void display(Shader &sh);
};

#endif //LEARNOPENGL_OBJETO_H