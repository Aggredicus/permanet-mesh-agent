from permanet_agent.commands.parser import CommandParser


def test_parser_ignores_unsummoned_public_chatter():
    parser = CommandParser()
    assert parser.parse("hello mesh") is None


def test_parser_reads_ping_command():
    parser = CommandParser()
    command = parser.parse("@permanet ping")
    assert command is not None
    assert command.name == "ping"
    assert command.args == ""


def test_parser_reads_ask_args():
    parser = CommandParser()
    command = parser.parse("@permanet ask what plants stabilize wet clay?")
    assert command is not None
    assert command.name == "ask"
    assert command.args == "what plants stabilize wet clay?"


def test_empty_summon_defaults_to_help():
    parser = CommandParser()
    command = parser.parse("@permanet")
    assert command is not None
    assert command.name == "help"
