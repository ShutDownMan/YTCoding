%%manim -ql -v WARNING ExpandingFactorial

class ExpandingFactorial(Scene):
    def construct(self):
        # show equation with n
        math_tex = MathTex(r"n!", substrings_to_isolate="!")
        math_tex.scale_to_fit_height(1.5)

        self.play(Write(math_tex))
        self.wait()
        
        # n! =
        fact_lhs, fact_rhs = (r"n! = ", r"")
        math_tex_new = MathTex(fact_lhs + fact_rhs)
        math_tex_new.scale_to_fit_height(1.1)
        math_tex_new.to_edge(LEFT)

        self.play(math_tex.animate.to_edge(LEFT), ReplacementTransform(math_tex, math_tex_new))
        self.wait()
        
        math_tex = math_tex_new
#         self.remove(math_tex_new)

        # 5! =
        fact_lhs, fact_rhs = (r"5! =", r"")
        math_tex_new = MathTex(fact_lhs + fact_rhs, substrings_to_isolate="=")
        math_tex_new.scale_to_fit_height(1.1)
        math_tex_new.to_edge(LEFT)

        self.play(ReplacementTransform(math_tex, math_tex_new))
        self.wait()
        
        math_tex = math_tex_new
#         self.remove(math_tex_new)

        # 5! = 5!
        fact_lhs, fact_rhs = (r"5! = ", r"5!")
        math_tex_new = MathTex(fact_lhs + fact_rhs, substrings_to_isolate=("=", "!"))
        math_tex_new.scale_to_fit_height(1.1)
        math_tex_new.to_edge(LEFT)

        self.play(ReplacementTransform(math_tex[-1], aux := math_tex_new[-3:]))
        self.wait()
        
#         print(aux)
#         self.remove(aux)
#         self.wait(3)
        
        math_tex = math_tex_new

        # 5! = rest of equation
        for i in reversed(range(5)):
#             fact_lhs, fact_rhs = (r"5! = ", r"5 \cdot 4!")
            fact_rhs = fact_rhs.replace('!', r" \cdot " + str(i) + r"!")

            math_tex_new = MathTex(fact_lhs + fact_rhs, substrings_to_isolate=("=", "\cdot", "!"))
            math_tex_new.scale_to_fit_height(1.1)
            math_tex_new.to_edge(LEFT)

            print(math_tex.submobjects)
            print(math_tex_new.submobjects)

            self.play(ReplacementTransform(math_tex[-1], math_tex_new[-3:]))
            self.wait()

            math_tex = math_tex_new

        # 0! = 1
        fact_rhs = fact_rhs.replace('0!', '1')
        math_tex_new = MathTex(fact_lhs + fact_rhs, substrings_to_isolate=("=", "\cdot", "!"))
        math_tex_new.scale_to_fit_height(1.1)
        math_tex_new.to_edge(LEFT)

        print(math_tex.submobjects)
        print(math_tex_new.submobjects)
        
        self.play(ReplacementTransform(math_tex[-2:], math_tex_new[-1:]))
        self.wait()
        
        math_tex = math_tex_new
#         self.remove(math_tex_new)

            
